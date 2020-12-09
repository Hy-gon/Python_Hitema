count=0

until [ $count -gt 5 ]
do
    echo count: $count
    ((count=count+1))
done
