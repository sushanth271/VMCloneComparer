echo "Comparing Network Parameters of the two VMs"
python examineNetwork.py $1 $2
echo "Comparing Compute Parameters of the two VMs"
python examineCompute.py $1 $2
