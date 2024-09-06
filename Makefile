tiss28:
	-npx --no-progress-bar promptfoo@latest eval --no-progress-bar --verbose
	npx promptfoo@latest view -y

clean:
	rm -r *~ \#* __pycache__ node_modules 
view:
	npx promptfoo@latest view -y
