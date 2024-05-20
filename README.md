# Ice-Breaker
<!DOCTYPE html>
<html lang="en">
<body>
<h2>1. Project Overview</h2>
<p><i>Ice Breaker</i> utilizes  <b>Langchain</b> in a <b>Flask-based</b> web application designed to streamline professional networking by providing insightful icebreakers and detailed summaries based on LinkedIn profiles. It uses advanced language models to generate content that can help facilitate more meaningful connections at networking events or in professional settings.</p>
<p>Given a user's name, a langchian is invoked using gpt 3.5 turbo returning a summary, ice breaker, topics of interest, and some facts about that person. This entails using a react agent to scrape the web and find the LinkedIn URL of the given name using custom-made tools and using  ProxyURL API to scrape that individual's LinkedIn.</p>
<h3>Demo</h3>
<p>Here is a link to the demo on youtube: https://www.youtube.com/watch?v=Xltc-nLsSKo</p>
<img src="https://github.com/Papakobina/Ice-Breaker/blob/main/homepage-Ice_breaker.png"></img>
  <h2>2. Technology Stack</h2>
    <ul>
        <li>Frontend: HTML, CSS, JavaScript, jQuery</li>
        <li>Backend: Flask, Python</li>
        <li>Language Processing: LangChain, LLM's OpenAI GPT-3.5 Turbo</li>
        <li>APIs: LinkedIn (via ProxyCurl), tavily_search, custom scraping tools</li>
        <li>Environment Management: <code>dotenv</code> for managing environment variables</li>
    </ul>

  <h2>3. Things Learned</h2>
    <p>This project was my initial foray into integrating large language models with web technologies. Key learnings include:</p>
    <ul>
        <li>Setting up and using LangChain with OpenAI's models to process and generate natural language content.</li>
        <li>Implementing and managing API calls, especially handling dynamic data scraping and processing.</li>
        <li>Enhancing Flask applications with advanced language processing capabilities.</li>
        <li>Developing efficient data parsing and cleaning techniques to ensure quality input for language models.</li>
        <li>Utilizing the different aspects of prompt engineering to receive efficient outputs</li>
    </ul>

  <h2>4. Technical Explanation</h2>
    <p>The application architecture is designed around several core components:</p>
    <ul>
        <li><strong>LangChain Integration:</strong> Utilizes LangChain to bridge Flask with OpenAI's GPT-3.5 Turbo, enabling sophisticated text generation and processing.</li>
        <li><strong>Flask Server:</strong> Manages web requests, serving HTML and processing form data. The server uses environment variables managed by <code>dotenv</code> for configuration, ensuring sensitive information remains secure.</li>
        <li><strong>LinkedIn Data Retrieval:</strong> Implements a robust LinkedIn scraping mechanism. If in mock mode, it fetches predefined JSON; otherwise, it uses a secured API endpoint to scrape real-time data.</li>
        <li><strong>Data Processing:</strong> The retrieved LinkedIn data undergoes parsing where unnecessary fields are filtered out and data is structured for further processing.</li>
        <li><strong>Content Generation:</strong> A series of prompts guide the language model to generate a summary, interesting facts, ice breakers, and topics of interest based on LinkedIn data, which are then formatted and returned to the user.</li>
    </ul>

  <h2>5. Next Steps to Improve on the Application</h2>
    <p>Future enhancements will focus on both functionality and user experience:</p>
    <ul>
        <li><strong>User Authentication:</strong> Implement OAuth to allow users to log in with their LinkedIn accounts, providing a personalized experience.</li>
        <li><strong>Interactive UI:</strong> Enhance the front-end to include interactive elements that allow users to customize the information they want to generate.</li>
        <li><strong>API Robustness:</strong> Introduce error handling and retries for API requests to improve reliability and user experience.</li>
        <li><strong>Expand Language Model Use:</strong> Explore more sophisticated prompts and fine-tuning of the language model to improve the relevance and accuracy of generated content.</li>
        <li><strong>Deployment and Scalability:</strong> Prepare the application for deployment on a cloud platform like Heroku and ensure it can scale to handle multiple users simultaneously.</li>
    </ul>

</body>
</html>
