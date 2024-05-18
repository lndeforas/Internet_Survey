F="all_questions"
F2="comp"
#mkdir $F $F/p4_adhd $F/p4_anx $F/p4_ang $F/p4_dep $F/everyone

LIST_DISEASES="p4_adhd p4_anx p4_sh p4_dep p4_ang p4_repet p4_sleep everyone"
LIST_QUESTIONS="5 6 7 8 9 10 11 12"

for i in $LIST_DISEASES
do
    for j in $LIST_QUESTIONS
    do
        python3 script_all_questions.py $i $j $F
        #python3 script_compare.py $i $j $F2 > $F2/$i/$j\_output
    done
done

python3 script_demography.py "demography" "demography" $F > $F/demography/demo_output