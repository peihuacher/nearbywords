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
Using the qwerty keyboard dictionary, the output will be<br>
```
['cat', 'car', 'ca5', 'ca6', 'cay', 'cah', 'cag', 'caf', 'cqt', 'cqr', 'cq5', 'cq6', 'cqy', 'cqh', 'cqg', 'cqf', 'cwt', 'cwr', 'cw5', 'cw6', 'cwy', 'cwh', 'cwg', 'cwf', 'cst', 'csr', 'cs5', 'cs6', 'csy', 'csh', 'csg', 'csf', 'cxt', 'cxr', 'cx5', 'cx6', 'cxy', 'cxh', 'cxg', 'cxf', 'czt', 'czr', 'cz5', 'cz6', 'czy', 'czh', 'czg', 'czf', 'xat', 'xar', 'xa5', 'xa6', 'xay', 'xah', 'xag', 'xaf', 'xqt', 'xqr', 'xq5', 'xq6', 'xqy', 'xqh', 'xqg', 'xqf', 'xwt', 'xwr', 'xw5', 'xw6', 'xwy', 'xwh', 'xwg', 'xwf', 'xst', 'xsr', 'xs5', 'xs6', 'xsy', 'xsh', 'xsg', 'xsf', 'xxt', 'xxr', 'xx5', 'xx6', 'xxy', 'xxh', 'xxg', 'xxf', 'xzt', 'xzr', 'xz5', 'xz6', 'xzy', 'xzh', 'xzg', 'xzf', 'dat', 'dar', 'da5', 'da6', 'day', 'dah', 'dag', 'daf', 'dqt', 'dqr', 'dq5', 'dq6', 'dqy', 'dqh', 'dqg', 'dqf', 'dwt', 'dwr', 'dw5', 'dw6', 'dwy', 'dwh', 'dwg', 'dwf', 'dst', 'dsr', 'ds5', 'ds6', 'dsy', 'dsh', 'dsg', 'dsf', 'dxt', 'dxr', 'dx5', 'dx6', 'dxy', 'dxh', 'dxg', 'dxf', 'dzt', 'dzr', 'dz5', 'dz6', 'dzy', 'dzh', 'dzg', 'dzf', 'fat', 'far', 'fa5', 'fa6', 'fay', 'fah', 'fag', 'faf', 'fqt', 'fqr', 'fq5', 'fq6', 'fqy', 'fqh', 'fqg', 'fqf', 'fwt', 'fwr', 'fw5', 'fw6', 'fwy', 'fwh', 'fwg', 'fwf', 'fst', 'fsr', 'fs5', 'fs6', 'fsy', 'fsh', 'fsg', 'fsf', 'fxt', 'fxr', 'fx5', 'fx6', 'fxy', 'fxh', 'fxg', 'fxf', 'fzt', 'fzr', 'fz5', 'fz6', 'fzy', 'fzh', 'fzg', 'fzf', 'vat', 'var', 'va5', 'va6', 'vay', 'vah', 'vag', 'vaf', 'vqt', 'vqr', 'vq5', 'vq6', 'vqy', 'vqh', 'vqg', 'vqf', 'vwt', 'vwr', 'vw5', 'vw6', 'vwy', 'vwh', 'vwg', 'vwf', 'vst', 'vsr', 'vs5', 'vs6', 'vsy', 'vsh', 'vsg', 'vsf', 'vxt', 'vxr', 'vx5', 'vx6', 'vxy', 'vxh', 'vxg', 'vxf', 'vzt', 'vzr', 'vz5', 'vz6', 'vzy', 'vzh', 'vzg', 'vzf']
```
```
['cat', 'car']
```
