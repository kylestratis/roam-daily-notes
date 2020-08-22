# roam-daily-notes
Alfred workflow that generates a Roam daily notes template

This workflow allows you to use a snippet trigger with [Alfred](https://www.alfredapp.com/) to generate daily notes. The top-level attributes should be replaced with habits you would like to track, and can use a an attr-table to build a quick habit tracker.

It also provides a space for Morning Pages. This is a space to start your day with some intentionality. You should have a separate page of questions and writing prompts, and drag blockrefs of 2 or 3 questions or prompts to answer for the day. My Morning Pages page looks like this:
- Questions
    - What am I excited about? 
    - What am I worried about? 
    - Is there anything I'm forgetting?
    - What would I like to write about?
    - What's bothering me? 
    - What do I need to prioritize? 
- Prompts
    - I love it when
    - I hate it when 
    - When I wake up
    - When I go to sleep 
    - If I could change one thing, it would be 
    - Next year I want to
    - I miss

At the end, it provides a space for a retrospective/time sieve (as described by Roam forum user mattbrockwell [in this thread](https://forum.roamresearch.com/t/what-would-be-your-top-3-tips-for-beginners/255)) to review your notes from the past. You can open these pages in the sidebar and potentially gain new insights into who you were, what you found important, and perhaps even something you're working on in the current day.

## Installation
To install, all you need to do is download the Roam Daily Notes.alfredworkflow file from this repo and
open it with Alfred. Define the snippet trigger you want to use (I like `\\xrdn`) and use it whenever you
want to generate your daily notes. The script that generates the template is also available to look
at in this repo. 

## Output
An example output looks like this: 
```
[[Morning Pages]]
[[Daily Mantras]]
Meditate:: ---
Gym/Exercise::
Read for pleasure::
Read for learning::
Greek::
Bass::
Retrospective
    One week ago: [[July 30th, 2020]]
    Four weeks ago: [[July 9th, 2020]]
    Twelve weeks ago: [[May 14th, 2020]]
    365 days ago: [[August 7th, 2019]]
```  
