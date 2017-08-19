from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

def analyze(text_to_analyze):
	client = language.LanguageServiceClient()
	document = types.Document(
		content=text_to_analyze,
		type=enums.Document.Type.PLAIN_TEXT)
	annotations = client.analyze_sentiment(document=document)
	return annotations

def get_result(annotations):
	score = annotations.document_sentiment.score
	magnitude = annotations.document_sentiment.magnitude
	dict = {'score': score, 'magnitude': magnitude}
	return dict


