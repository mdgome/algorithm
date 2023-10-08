# Questions

Let's learn about list comprehensions! You are given three integers $x, y$ and $n$ representing the dimensions of a cuboid along with an integer $n$. Print a list of all possible coordinates given by $(i, j, k)$ on a 3D grid where the sum of $(i, j, k)$ is not equal to $n$. Here, $0 <= i <= x;0 <= j <= y;0 <= k <= z$ . Please use list comprehensions rather than multiple loops, as a learning exercise.

**Example**

`x = 1`

`y = 1`

`z = 2`

`n = 3`

All permutations of $[i, j, k]$ are:

$[[0,0,0], [0,0,1], [0,0,2], [0,1,0], [0,1,1], [0,1,2], [1,0,0], [1,0,1], [1,0,2], [1,1,0], [1,1,1], [1,1,2]]$

Print an array of the elements that do not sum to $n = 3$.

$[[0,0,0], [0,0,1], [0,0,2], [0,1,0], [0,1,1], [1,0,0], [1,0,1], [1,1,0], [1,1,2]]$

**Input Format**

Four integers $x, y, z$ and $n$, each on a separate line.

**Constraints**

Print the list in lexicographic increasing order.

**Sample Input 0**

```jsx
1
1
1
2
```

**Sample Output 0**

```jsx
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
```

**Explanation 0**

Each variable $x, y$ and $z$ will have values of $0$ or $1$ . All permutations of lists in the form 

.

Remove all arrays that sum to  to leave only the valid permutations.

**Sample Input 1**

```jsx
2
2
2
2
```

**Sample Output 1**

```jsx
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]
```

# Answer

```python
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    result = []
    for i in range(x+1) :
        for j in range(y+1) :
            for k in range(z+1) :
                if (i+j+k) != n :
                    result.append([i,j,k])
    # result = [(i,j,k) for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k != n) ]
    print(result)
```

# 해석

i, j, k 를 1씩 i 다음 j 다음 k 순으로 증가시키며 i + j + k 가 n이 아닌 경우만 리스트에 담는다.