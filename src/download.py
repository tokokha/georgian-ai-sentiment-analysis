from huggingface_hub import snapshot_download

snapshot_download(repo_id="RichNachos/georgian-corpus", repo_type="dataset", local_dir="corpora")