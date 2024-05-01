F="all_questions_v2"
#mkdir $F $F/p4_adhd $F/p4_anx $F/p4_ang $F/p4_dep $F/everyone

LIST_DISEASES="p4_adhd p4_anx p4_sh p4_dep p4_ang p4_repet p4_sleep everyone"
LIST_QUESTIONS="p5 p6 p7 p8 p9 p10 p11 p12 a5 a6 a7 a8 a9 a10 a11 a12"

for i in $LIST_DISEASES
do
    for j in $LIST_QUESTIONS
    do
        python3 script_all_questions.py $i $j $F > $F/$i/$j\_output
    done
done

python3 script_demography.py > $F/demography/demo_output