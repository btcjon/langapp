from langchain.document_loaders import (
    CSVLoader,
    FileDirectoryLoader,
    HTMLLoader,
    MarkdownLoader,
    PDFLoader,
    XMLLoader,
    YoutubeTranscriptLoader,
    YoutubeAudioLoader,
    WebBaseLoader,
    URLLoader,
    TwitterLoader,
    SitemapLoader,
    RecursiveURLLoader,
)


# Initialize the loaders
csv_loader = CSVLoader()
file_directory_loader = FileDirectoryLoader()
html_loader = HTMLLoader()
markdown_loader = MarkdownLoader()
pdf_loader = PDFLoader()
xml_loader = XMLLoader()
youtube_transcript_loader = YoutubeTranscriptLoader()
youtube_audio_loader = YoutubeAudioLoader()
web_base_loader = WebBaseLoader()
url_loader = URLLoader()
twitter_loader = TwitterLoader()
sitemap_loader = SitemapLoader()
recursive_url_loader = RecursiveURLLoader()

# Specify the paths or URLs for the loaders
csv_path = "path_to_your_csv_file"
directory_path = "path_to_your_directory"
html_path = "path_to_your_html_file"
markdown_path = "path_to_your_markdown_file"
pdf_path = "path_to_your_pdf_file"
xml_path = "path_to_your_xml_file"
youtube_video_id = "your_youtube_video_id"
webpage_url = "https://www.example.com"
twitter_username = "your_twitter_username"
sitemap_url = "https://www.example.com/sitemap.xml"

# Load the documents
csv_documents = csv_loader.load(csv_path)
file_directory_documents = file_directory_loader.load(directory_path)
html_documents = html_loader.load(html_path)
markdown_documents = markdown_loader.load(markdown_path)
pdf_documents = pdf_loader.load(pdf_path)
xml_documents = xml_loader.load(xml_path)
youtube_transcript_documents = youtube_transcript_loader.load(youtube_video_id)
youtube_audio_documents = youtube_audio_loader.load(youtube_video_id)
web_base_documents = web_base_loader.load(webpage_url)
url_documents = url_loader.load(webpage_url)
twitter_documents = twitter_loader.load(twitter_username)
sitemap_documents = sitemap_loader.load(sitemap_url)
recursive_url_documents = recursive_url_loader.load(webpage_url, depth=2)
