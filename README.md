# Sentiment Analysis of AI in Georgian Media

A comprehensive analysis of how artificial intelligence is discussed and perceived in Georgian media using BERTopic and transformer-based sentiment classification.

## Overview

This project analyzes Georgian-language media discourse surrounding artificial intelligence through three complementary analytical approaches:
- **Volume Analysis**: Identifies major publishers and distribution patterns
- **Topic Modeling**: Uncovers thematic discussions about AI using BERTopic
- **Sentiment Analysis**: Assesses media sentiment toward AI technology

The analysis draws from 15,904 contextual passages extracted from the Common Crawl dataset, providing insights into Georgian public perception of emerging technology.

## Dataset

- **Source**: Common Crawl repository
- **Original Size**: 5,333,536 documents
- **Processed Dataset**: 15,904 entries (3-sentence contextual windows around AI mentions)
- **License**: GPL-3.0
- **Attribution**: Built on the [Georgian Corpus dataset](https://huggingface.co/datasets/RichNachos/georgian-corpus)

## Methodology

### Data Preparation

1. **Integration**: Merged distributed parquet files from the Georgian Corpus dataset into unified corpus
2. **Contextual Extraction**: For each mention of "ხელოვნური ინტელექტი" (artificial intelligence), extracted a 3-sentence window (target sentence + 1 before and after) to maintain semantic context
3. **Preprocessing**: Applied text normalization, rule-based stemming for Georgian morphology, and stopword removal (40+ function words)

### Volume Analysis

- Domain extraction via URL parsing
- Publisher frequency analysis
- Media concentration assessment (top 20 domains vs. all sources)

### Topic Modeling

**Model**: BERTopic with the following configuration:
- **Embeddings**: `paraphrase-multilingual-mpnet-base-v2` (multilingual sentence transformer)
- **Dimensionality Reduction**: UMAP (15 neighbors, 2 components, cosine distance)
- **Clustering**: HDBSCAN (minimum cluster size: 40 documents, EOM selection)
- **Topic Representation**: Custom CountVectorizer (1-2 grams, min/max document frequency thresholds)
- **Outlier Reduction**: Three-stage strategy (c-TF-IDF, embedding-based, probability-based)
- **Temporal Analysis**: 20 temporal bins to track topic evolution over time

### Sentiment Analysis

**Model**: GeorgianBert-Sent (fine-tuned BERT for Georgian sentiment classification)
- **Classification**: 4-class (positive, neutral, negative, mixed)
- **Input**: Context passages to capture AI-specific sentiment rather than document-level sentiment
- **Processing**: GPU-accelerated batch processing (batch size: 32)

## Project Structure

```
georgian-ai-sentiment-analysis/
├── README.md
├── LICENSE (GPL-3.0)
├── requirements.txt
├── .gitignore
├── data/
│   └── processed_corpus.parquet
├── notebooks/
│   ├── volume_analysis.ipynb
│   ├── topic_analysis.ipynb
│   └── sentiment_analysis.ipynb
└── src/
    ├── download.py
    └── getdata.ipynb
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/tokokha/georgian-ai-sentiment-analysis.git
cd georgian-ai-sentiment-analysis
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run notebooks in order:
```
getdata.ipynb → topic_analysis.ipynb → sentiment_analysis.ipynb → volume_analysis.ipynb
```

## Dependencies

See `requirements.txt` for specific versions.

- **Future Improvements**:
  - Expand analysis to other Georgian language sources
  - Comparative analysis with other language media

## Data & Model Attribution

**Dataset**: [Georgian Corpus](https://huggingface.co/datasets/RichNachos/georgian-corpus) - GPL-3.0 License

**Sentiment Analysis Model**: [GeorgianBert-Sent](https://huggingface.co/Arseniy-Sandalov/GeorgianBert-Sent)

### Citation

If you use the **GeorgianBert-Sent** model (used in this project for sentiment classification), please cite:

```bibtex
@misc{Stefanovitch2023Sentiment,
  author = {Stefanovitch, Nicolas and Piskorski, Jakub and Kharazi, Sopho},
  title = {Sentiment analysis for Georgian},
  year = {2023},
  publisher = {European Commission, Joint Research Centre (JRC)},
  howpublished = {\url{http://data.europa.eu/89h/9f04066a-8cc0-4669-99b4-f1f0627fdbbf}},
  url = {http://data.europa.eu/89h/9f04066a-8cc0-4669-99b4-f1f0627fdbbf},
  type = {dataset},
  note = {PID: http://data.europa.eu/89h/9f04066a-8cc0-4669-99b4-f1f0627fdbbf}
}
```

## License

This project is distributed under the GPL-3.0 License. See LICENSE file for details.

## Contact

Tornike Khabeishvili
tornikekhabeishvili07@gmail.com