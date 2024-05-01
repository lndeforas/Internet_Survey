RAWF="devices_raw_outputs"
#mkdir $RAWF

LIST="p4_adhd p4_anx p4_sh p4_dep p4_ang p4_repet p4_sleep ' ' ,"

for i in $LIST
do
    python3 script_devices.py $i > $RAWF/$i\_devices_output
    python3 script_comp_laptop.py $i > $RAWF/$i\_comp_devices_output
done

python3 script_demography.py > $RAWF/demo_output