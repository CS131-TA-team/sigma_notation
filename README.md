# Macro Example 1: Sigma Notation

This example shows how to define a sigma notation macro,
which calculates summations of products
over the some indices that only occurs on the right hand side.

For example:

```text
#Σ[(c i k) (a i j) (b j k)]
```
means `assign c[j,k] with the sum of a[i,j]*b[j,k] over j`, i.e.
$$ c_{i,k} =  \sum_{j} {a_{i,j}b_{j,k}} \forall j $$

```text
#Σ[(s k) (x i) (y j) (w i j k)]
```
means `assign s[k] with the sum of x[i]*y[j]*w[i,j,k] over (i,j)`.

