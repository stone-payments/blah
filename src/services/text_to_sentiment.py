# [START import_libraries]
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
# [END import_libraries]
# [START def_analyze]
def analyze(textToAnalyze):
	"""Run a sentiment analysis request on text within a passed filename."""
	client = language.LanguageServiceClient()
	document = types.Document(
		content=textToAnalyze,
		type=enums.Document.Type.PLAIN_TEXT)
	annotations = client.analyze_sentiment(document=document)
	# Print the results    
	return annotations
# [END def_analyze]

# [START def_print_result]
def get_result(annotations):
	score = annotations.document_sentiment.score
	magnitude = annotations.document_sentiment.magnitude
	dict = {'score': score, 'magnitude': magnitude}
	return dict
# [END def_print_result]


