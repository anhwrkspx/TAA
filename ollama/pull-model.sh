./bin/ollama serve &

sleep 5

echo "Pull model deepseek"

ollama pull gemma3:1b
