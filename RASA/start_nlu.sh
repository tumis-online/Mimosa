echo "Running $0"
echo "Installing RASA dependencies..."
echo "Installing SpaCy dependencies..."
pip3 install rasa[spacy]
python3 -m spacy download en_core_web_md

echo "Starting and NLU Server..."
rasa run --enable-api -m "$1"