# SuperDARN Radar Schedule Maker
The radar schedule maker generates site specific schedule files based on the provided generic schedule file.
## Install Radar Schedule Maker
1. Install the necessary packages
   - Python 3
2. Clone the git hub repository to your local machine
3. Update the SuperDARN SWG provided schedule file, run:  
`git submodule update --remote`
4. Install the "schedule_files" directory at the same level as "radar_schedule_maker"  
  
Directory Structure  
|  
| - radar_schedule_maker/  
| | - external/  
| | - tests/    
|  
| - schedule_files/  
| | - kod/  
| | - mcm/  
| | - sps/  
| | - ade/  
| | - adw/  

## Run Radar Schedule Maker
1. Update the SuperDARN SWG provided schedule file, run:  
`git submodule update --remote`
1. Run Scheduler using:  
`python3 schedule_maker.py -a --sitelist kod.d mcm.a sps.a`  
(This generates schedule for Kodiak, McMurdo, and South Pole)  

### Arguments and Flags  
1. Sites - There are two ways to specify the sites  
   1. `--sitelist`  
     Specify the radar(s) and channel(s) in \<site id\>.\<channel letter\> format, takes a list of arguments  
   1. `--site` and `--channel`  
   Specify the site ids in a list following `--site` and the channel letter following `--channel`.
   The scheduler will create schedules for all site and channel combinations.  
1. `--year` or `-y` - Specify the desired year of the schedule file, defaults to the year of the previous month.
1. `--month` or `-m` - Specify the desired month of the schedule file, defaults to the previous month.
1. `--header` - Prints the header for the radar before the schedule. This should only be used for new files.
1. `--append` or `-a`- Appends the new schedule to the end of an existing radar specific schedule file.
1. `--auto` - Removes user prompts to allow the script to run in an automated way.