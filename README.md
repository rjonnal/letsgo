# Lissajous Eye Trace Statistical GOodies (LETSGO)

This library contains convenience functions for working with data from the Lissajous eye tracking system. It is intended to assist with organization of CSV files and conversion of CSV files into [Pandas](https://pandas.pydata.org/) data structures. See the `/examples` folder for some illustrative minimum working examples.

## Overview of data processing pipeline

The data processing pipeline for eye tracking data consists of three steps:

1. Calculation of trajectories from the SLO image, using INOKO software.
2. Calculation of figures of merit, e.g. bivariate contour ellipse area (BCEA), using Valentyna's software. These are stored in the files described below.
3. Hypothesis-driven statistical analysis and visualization, using this library.

## Quick start

Note: I use the word 'terminal' in the ordinary way for Linux and Mac users, but Windows users should use Anaconda PowerShell (not Anaconda Prompt).

1. Install a programmer-friendly text editor such as [emacs](https://www.gnu.org/software/emacs/) in Linux, or [Notepad++](https://notepad-plus-plus.org/download) in Windows. If you're more advanced and accustomed to debugging tools, you may prefer VSCode. And if you're a MATLAB user you may prefer Spyder, which is bundled with Anaconda.
2. Install Git using your package manager (or by visiting [the Git download site](https://git-scm.com/download/) for Windows).
3. Install [Anaconda for Python 3.X+](https://www.anaconda.com/download#downloads)
4. If necessary, create a folder where your Python libraries will reside. Conventions in my lab are `~/code/` on Linux machines (and derivatives like macOS) and `C:\code\` on Windows machines.
5. Add that folder to the environment variable `PYTHONPATH`. If your computer doesn't have this environment variable set yet, then create the variable and define it as the location where you will store Python libraries. If the variable exists, then append the folder from step 4 to its definition. In Linux, add `export PYTHONPATH="${PYTHONPATH}:/home/YOURUSERNAME/code"` to the bottom of your `~/.bashrc` file, and restart the terminal. Replace `YOURUSERNAME` with your Linux username. This will create the variable `PYTHONPATH` if it doesn't exist and define it as `/home/YOURUSERNAME/code`. If it exists, it will append `/home/YOURUSERNAME/code` to the existing definition. For other OS's: [Windows](https://optics.ansys.com/hc/en-us/articles/7812289531923-Create-or-modify-environment-variables-in-Windows), [Mac](https://apple.stackexchange.com/questions/381655/how-to-and-should-i-put-a-path-to-user-installed-python-ahead-of-system-instal).
5. Open `Anaconda prompt` and type `cd c:/code` or `cd ~/code` to navigate to the relevant folder.
6. Clone this repository into that folder by typing: `git clone https://github.com/rjonnal/letsgo`.
7. If `git clone` doesn't work, you can download LETSGO as a [zip file](https://github.com/rjonnal/letsgo/archive/refs/heads/main.zip) instead, and unzip it into the Python library folder you created in (4).
8. Download and unzip some example data.
9. Open one of the scripts in `letsgo/examples` using your text editor, and edit it to point it to the example data.
10. Navigate to the examples folder in the terminal, e.g. `cd c:\code\letsgo\examples` or `cd ~/code/letsgo/examples`.
11. Run the example: `python 00_load_data.py`.

## Slightly slower start

1. Take the time to learn a few commands for the Anaconda prompt. [Here is a quick guide.](https://medium.com/@marsmans/learning-to-use-the-terminal-ccd1595250e5)
2. Take a few-hour Python tutorial. [W3schools](https://www.w3schools.com/python/python_intro.asp) has a good introductory tutorial. [Codecademy](https://www.codecademy.com/catalog/language/python) has many more specialized tutorials, some of which are free.


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
   ...trajectories.csv
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
   2026-07-07_13-32-34_trajectories.csv
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

## Example scripts

In `letsgo/examples` are scripts meant to illustrate the basic functionality of `letsgo` and general approaches for data analysis problems. When someone in the group wants to know how to do something, I'll illustrate by creating a new example script and adding it to the repo. At present the following scripts are available:

### `letsgo/examples/00_load_data.py`

**`letsgo/examples/01_plotting_trajectories.py`**

`letsgo/examples/02_reorganize_files.py`

`letsgo/examples/03_coefficient_of_variation.py`

`letsgo/examples/04_coefficient_of_variation_multi_session.py`

`letsgo/examples/05_ttest_and_histograms.py`
