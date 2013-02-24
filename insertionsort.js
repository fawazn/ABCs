//Simple insertion sort function in Javascript

function insertionsort (a) {

  for (i = 0; i<a.length; i++)
    for (j = i; j>0 && a[j]<a[j-1]; j--)
    {  tmp = a[i];
      a[a.indexOf(min)] = tmp;
      a[i] = min;
    }
  return a;
}
  document.write(insertionsort([56,74,345,12,34,45,23]));
