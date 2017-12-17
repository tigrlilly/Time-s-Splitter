# Time-s-Splitter
Time(s) Splitter is a split and concatenate tool inspired by the cut-up method of William Burroughs.

README Time(s) Splitter

Time(s) Splitter is a generative scripting framework that splits and concatenates lines of text per
a structured disorder laid out by Python query language. The project was inspired by the cut-up
method of William Burroughs and uses the New York Times api in honor of Burroughs’s
sourcing newspapers as material. See the deployment section on how to initialize the project on
a live system.

GETTING STARTED
These instructions provide a copy of the project and guide their set up on your local machine.
See script detail notes for details on the reasoning behind programming decisions.

PREREQUISITES
Before you get started, you will need to request an API-key to the New York Times, or any
source of your choosing, and any software to write a CSV to. The API-key that I used from the
Times was their Article Search API that may be found here,
https://developer.nytimes.com/article_search_v2.json
Import your requests, json (in the case of the New York Times api), and csv.

SCRIPT DETAILS
Download and open the “oldest” and “newest” Python scripts in your preferred text editor. The
leading request is written specifically for the Times Article Search API, insert and amend any
other filter aspects of the Times Article Search JSON features, here. Note, I was really only
using one request based on date to set a temporal scope of Burroughs’s birth and death dates. I
flipped the chronological order of the returns to actually give me two different results. You may
switch the order of returns by specifying “sort:” as “newest” or “oldest”. These two returns
provided the basis of my two different files to concatenate.

DECONSTRUCTING/SPLITTING
The next step to working with your returns is the process of splitting. I used a three-part
“if” statement based upon how lines of text were already naturally joined. I deconstructed
lines based on those natural joins or pauses. So, I split on commas first, then “and”, then
“in|on|that|for”.

RECONSTRUCTING/CONCATENATING
You then print the split strings to rows on a CSV. You do this for your two, or however
many requests you wish to make. My two requests generated two CSVs, an “oldest” and
a “newest”. A third Python scripting file will allow you to reassemble and join the two
CSVs. Begin this third Python script by importing csv—old data and new data. Now you
need to specify how you would like to concatenate “lines,” rather rows, of text. The
“stitchedString” function sets up an alternating pattern of joining one cell of text from one
csv to another. Not all blurbs of text are the same length so they would not alternate
evenly. Anticipating this, I cut blurbs to be symmetrical in length to make even patterns
with no trailing text that would not be left unaltered. You can see this function scripted
out from lines nine to nineteen of “newmaterial.py.”
Running “newmaterial.py” will provide you with a set of reconstructed lines from your
source material.
