# #!/bin/sh
cd ./backend
echo "Current working dir $(pwd)"

echo "Formatting code using black"
black ./app

echo "Linting code using pylint"
pylint ./app ./tests