if [ $1 == 'build' ]
then
docker build -t textractortechnologies/omop-abstrator-nlp .
fi

if [ $1 == 'push' ]
then
docker push textractortechnologies/omop-abstrator-nlp:latest
fi

if [ $1 == 'run' ]
then
docker run --rm -d -p 80:80 textractortechnologies/omop-abstrator-nlp
fi
