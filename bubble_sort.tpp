{Autor: Ana Carolina Frozza}

inteiro: v[10]
inteiro: tam

tam := 10

preencheVetor()
  inteiro: i
  inteiro: j
    
  i := 0
  j := tam
  repita
    v[i] = j
    i := i + 1
    j := j - 1
  até i < tam
fim 

bubble_sort()
  inteiro: i
  i := 0
  repita
    inteiro: j
    j := 0
    repita
      se v[i] > v[j] então
        inteiro: aux
        aux := v[i]
        v[i] := v[j]
        v[j] := aux
      fim
      j := j + 1
    até j < i
    i := i + 1
  até i < tam
fim

inteiro principal()
  preencheVetor()
  bubble_sort()
  retorna(0)
fim