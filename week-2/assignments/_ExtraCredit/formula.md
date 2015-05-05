```
FOR CBC mode
# m[0] = D(k, c[0]) xor IV
# m[1] = D(k, c[1]) xor c[0]
# m[i] = D(k, c[i]) xor c(i-1)
```

```
For CTR Mode
# m[0] = E(k,IV) xor c[0]
# m[1] = E(k, IV + 1) xor c[1]
# m[i] = E(k, IV + i) xor c[i]
```
<br>
Related lectures:<br>
[1] <a href="https://github.com/ashumeow/cryptography-I/blob/master/week-2/notes/10%20-%20Modes%20of%20Operations%20:%20Many-Time%20key.md">notes-10</a>
