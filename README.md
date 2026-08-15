# Lissajous Eye Trace Statistical GOodies (LETSGO)

This library contains convenience functions for working with data from the Lissajous eye tracking system. It is intended to assist with organization of CSV files and conversion of CSV files into [Pandas](https://pandas.pydata.org/) data structures. See the `/examples` folder for some illustrative minimum working examples.

## Overview of data processing pipeline

The data processing pipeline for eye tracking data consists of three steps:

1. Calculation of trajectories from the SLO image, using INOKO software.
2. Calculation of figures of merit, e.g. bivariate contour ellipse area (BCEA), using Valentyna's software. These are stored in the files described below.
3. Hypothesis-driven statistical analysis and visualization, using this library.

## Ground rules

1. All eye tracking data is expected in CSV file format. There are no unusual limitations imposed by working with XSLX files, but it is more complicated and bug-prone, and we have to choose one or the other, so let's choose CSV.

2. We had to make an arbitrary choice between *merged* and *unmerged* data. We decided to work with *unmerged* data only, so we have to stick with that choice.

3. For a given measurement/trial, we expect **all** of the following files:

   ```
   ...distributional_aggregated.csv
   ...drift_non_aggregated.csv
   ...measurement_inform.csv
   ...non_distributional_parameters.csv
   ...pso_non_aggregated.csv
   ...saccade_non_aggregated.csv
   ...saccade_with_pso_non_aggregated.csv
   ...trial_non_aggregated.csv
   ```

   For example:

   ```
   2026-07-07_13-32-34_distributional_aggregated.csv
   2026-07-07_13-32-34_drift_non_aggregated.csv
   2026-07-07_13-32-34_measurement_inform.csv
   2026-07-07_13-32-34_non_distributional_parameters.csv
   2026-07-07_13-32-34_pso_non_aggregated.csv
   2026-07-07_13-32-34_saccade_non_aggregated.csv
   2026-07-07_13-32-34_saccade_with_pso_non_aggregated.csv
   2026-07-07_13-32-34_trial_non_aggregated.csv
   ```

4. Please be consistent in naming files, assigning patient codes, etc. Once the conventions have been determined, we can enumerate them here for reference. It is important, from a programming perspective, to always use '-' (or '_') between the date and time portions of filenames.

5. Experimenters must name a folder for storing data from an experiment. Tentatively: the convention for structuring folders is SSSSSS_XXX/SSSSSS_XXX_CC_TT: SSSSSS is study name, XXX is the patient/subject number, CC is the experimental condition, and TT is trial number. An example:

   ```bash
   ├── NeuroSleep_026
   │   ├── NeuroSleep_026_SD_01
   │   │   ├── 2026-07-09_13-14-14_distributional_aggregated.csv
   │   │   ├── 2026-07-09_13-14-14_drift_non_aggregated.csv
   │   │   ├── 2026-07-09_13-14-14_measurement_inform.csv
   │   │   ├── 2026-07-09_13-14-14_non_distributional_parameters.csv
   │   │   ├── 2026-07-09_13-14-14_pso_non_aggregated.csv
   │   │   ├── 2026-07-09_13-14-14_saccade_non_aggregated.csv
   │   │   ├── 2026-07-09_13-14-14_saccade_with_pso_non_aggregated.csv
   │   │   ├── 2026-07-09_13-14-14_trajectories.csv
   │   │   ├── 2026-07-09_13-14-14_trial_non_aggregated.csv
   │   │   ├── 2026-07-09_13-16-22_distributional_aggregated.csv
   │   │   ├── 2026-07-09_13-16-22_drift_non_aggregated.csv
   │   │   ├── 2026-07-09_13-16-22_measurement_inform.csv
   │   │   ├── 2026-07-09_13-16-22_non_distributional_parameters.csv
   │   │   ├── 2026-07-09_13-16-22_pso_non_aggregated.csv
   │   │   ├── 2026-07-09_13-16-22_saccade_non_aggregated.csv
   │   │   ├── 2026-07-09_13-16-22_saccade_with_pso_non_aggregated.csv
   │   │   ├── 2026-07-09_13-16-22_trajectories.csv
   │   │   ├── 2026-07-09_13-16-22_trial_non_aggregated.csv
   ```

## Reorganization of files

Generally, we will try to leave the organization and names of files alone, but with the following exception. The filenames listed above, all resulting from a single trial, are identical regardless of the experimental protocol (i.e., fixation, saccade, etc.). As a first step, to clarify the relevance of the files and directions for downstream analysis, these will be reorganized according to protocol. The function `letsgo.organize_by_protocol` takes a folder as an argument, inspects the `...measurement_inform.csv` file to determine the name of the protocol, and then moves files into subfolders according to protocol.