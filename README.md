# Feedbro-to-LibreTube
 Replaces subscriptions from [LibreTube](https://libre-tube.github.io/) with those exported by [Feedbro](https://nodetics.com/feedbro/).  

Basically I don’t really care to use an account for watching YouTube, so I use [Feedbro](https://nodetics.com/feedbro/) as a Firefox addon on my desktop and [LibreTube](https://libre-tube.github.io/) on my Android. To synchronize my “subscriptions” between them, I created this little script.  

*Warning:* This is a one way synchronization from [Feedbro](https://nodetics.com/feedbro/) to [LibreTube](https://libre-tube.github.io/). The current version doesn’t try to merge subscriptions and you cannot synchronize from [LibreTube](https://libre-tube.github.io/) to [Feedbro](https://nodetics.com/feedbro/). Maybe I will add this in the future, but right now this is simply not my use case.  

# Dependencies
Python3 for the Python version

# Usage
`./feedbro_to_libretube.py Feedbro-Subscriptions.opml LibreTubeSettings.json`  

The subscriptions in `LibreTubeSettings.json` will be replaced with subscriptions from [Feedbro](https://nodetics.com/feedbro/).  
After running this script, re-import the JSON file to replace your subscriptions .  

Steps to export [Feedbro](https://nodetics.com/feedbro/) subscriptions:
1. Open Feedbro
2. Go to the settings
3. Click the “Export as OPML” button
(You don’t need to filter for YouTube channels, the script will automatically extract them.)  

Steps to import [LibreTube](https://libre-tube.github.io/) subscriptions
1. Go to the “Settings” menu
2. Click on “Backup & Restore”
3. Click on “Restore” under the “App backup” section
4. Select `LibreTubeSettings.json`
