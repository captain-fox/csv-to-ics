This is a converter-tool that creates .ics events from my school's .csv schedule.

I'm building this tool using framework-ish architecture.
There will be 3 main stages of algorithm:
1. Import (importing csv, checking file format and fields)
2. Process (converts all the data to .ics friendly)
3. Event (Creating new .ics file, parsing gathered and processed data to it)