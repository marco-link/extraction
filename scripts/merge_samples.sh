#!/bin/bash


VERSION="2022-11-09_v10"
YEAR=2017


#prepare for more years and versions
if [ $1 ]
then
    VERSION=$1
fi

if [ $2 ]
then
    YEAR=$2
fi

#BASEPATH="root://cmsxrootd-kit.gridka.de//store/user/mlink/WbNanoAODTools"
BASEPATH="/eos/cms/store/cmst3/group/top/WbWb/WbNanoAODTools/"


OUTDIR="/eos/cms/store/cmst3/group/top/WbWb/nano/"

ALLSAMPLES=`list_samples.py $VERSION $YEAR --base_path $BASEPATH`

echo "merging ${ALLSAMPLES}"
echo

echo "merging to ${OUTDIR}/${VERSION}/${YEAR}"

DOIT="y"
if [ -d ${OUTDIR}/${VERSION}/${YEAR} ]
then
    echo "output dir already exists. Are you sure you want to continue merging unmerged files? (y/n)"
    read DOIT
fi

if [ ! $DOIT ] || [ $DOIT != 'y' ]
then
    echo "cancel"
    exit
fi

rm -f "${OUTDIR}/${VERSION}/${YEAR}/sample_list.txt"
rm -f "${OUTDIR}/${VERSION}/${YEAR}/merge_failed.txt"


for sample in $ALLSAMPLES
do

    FULLPATH="${BASEPATH}/${VERSION}/${YEAR}/${sample}/WbNanoAODTools_${VERSION}"
    OUTPATH="${OUTDIR}/${VERSION}/${YEAR}/${sample}"

    mkdir -p $OUTPATH
    # echo merging $FULLPATH to $OUTPATH ... "(${OUTPATH}/merge.log)"
    #continue
    {
        merge.py $FULLPATH $OUTPATH $YEAR  #> $OUTPATH/merge.log 2>&1

        if [ $? != 0 ];
        then
        echo $sample >> "${OUTDIR}/${VERSION}/${YEAR}"/merge_failed.txt
        else
        echo $sample >> "${OUTDIR}/${VERSION}/${YEAR}"/sample_list.txt
        fi
    }
    #exit

done
#wait
# exit
