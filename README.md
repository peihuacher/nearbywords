# nearbywords
Given a word find the nearby words. 

Assumption
- the nearby words are formed by adjacent characters of each characters in a word. 
- order of the word and its characters remain the same

The output will be <br>
```
['cat', 'cas', 'cau', 'czt', 'czs', 'czu', 'cbt', 'cbs', 'cbu', 'bat', 'bas', 'bau', 'bzt', 'bzs', 'bzu', 'bbt', 'bbs', 'bbu', 'dat', 'das', 'dau', 'dzt', 'dzs', 'dzu', 'dbt', 'dbs', 'dbu']
```
```
['cat', 'bat']
```

To cater to real-life data entry issues, we can change the dictionary in the get_nearby_chars() to nearby words in the qwerty keyboard using the dictionary below:<br>
```
nearby_qwerty_char = { # nearby words in qwerty keyboard
        'c': ['c','x','d','f','v'],
        'a': ['a','q','w','s','x','z'],
        't': ['t','r','5','6','y','h','g','f']
    }
```
