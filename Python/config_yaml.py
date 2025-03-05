#!/usr/bin/env python3

#!/usr/bin/env python3

# Python code

import yaml


with open("config.yaml") as f:
	cfg = yaml.load(f, Loader= yaml.FullLoader)
	print(cfg)

with open("config.yaml","w") as f:
	
	print(cfg)
	cfg= {}
	cfg["n_components"] = 0.2
	cfg["umap_params"] = {}
	cfg["umap_params"]["metrics"] = []
	cfg["umap_params"]["metrics"].append("chebyshev")
	print(cfg)
	cfg = yaml.dump(
		cfg, stream=f, default_flow_style=False, sort_keys=False
	)
	print(cfg)
	
print(cfg)