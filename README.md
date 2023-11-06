# json-processor
console python utility to edit json files.<br>
(Simple utility i wrote to edit level files in my game)<br>

# Commands
<pre>
Common form: `command [argument1]  [argumentn]  
`exit`         or `e`         - exit program, back to terminal<br>
`open file`    or `o`         - opens json files, throws error if it's not json or it doesn't exist<br>
`showk`        or `sk`        - shows keys with 10 elements on 1 line by default<br>
`change_ssn n` or `cn`        - change the number of printed keys on 1 line<br>
`save file```  or `s`         - write down created/changed json file<br>
`init`         or `i`         - creates empty json file, replacing opened/created file<br>
`addk key`     or `ak`        - adds new key<br>
`showv key`    or `sv`        - shows value of the key<br>
`change_val key val`  or `cv` - change value of key<br>

</pre>

# Modes
1) Interactive
  run json_processor.py and use commands above.

2) CLI
  pass the sequence of commands and they will be executed one by one. Every command must be finished with ;
  Example: ```json_processor.py o file.json; sk; addk new_key; cv new_key some_val;```
