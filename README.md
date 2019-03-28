### The code can detect the whether street information input by user is correct and compute the Edge and Vertices.

#### For example, Input

##### a "Weber Street" (2,-1) (2,2) (5,5) (5,6) (3,8)
##### a "King Street S" (4,2) (4,8)
##### a "Davenport Road" (1,4) (5,8)
##### g

### Then it will output 
##### V = {
##### 1: (2,2)
##### 2: (4,2)
##### 3: (4,4)
##### 4: (5,5)
##### 5: (1,4)
##### 6: (4,7)
##### 7: (5,6)
##### 8: (5,8)
##### 9: (3,8)
##### 10: (4,8)
##### }
##### E = {
##### <1,3>,
##### <2,3>,
##### <3,4>,
##### <3,6>,
##### <7,6>,
##### <6,5>,
##### <9,6>,
##### <6,8>,
##### <6,10>
##### }

### You can also modify or remove street Street
#### c "Weber Street" (2,1) (2,2)
#### r "King Street S"
#### Basically, it reads street information and output undirected graph.
