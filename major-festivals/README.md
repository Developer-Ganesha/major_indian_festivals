# Major Indian Festivals Web Application

An interactive web application that teaches users about major Indian festivals (Diwali, Harvest Festival, and Holi) through engaging content and quizzes.

## Features

- Interactive learning experience
- Step-by-step content presentation
- Quiz for each festival
- Combined quiz for all festivals
- 10-minute timer for the learning session
- Responsive design using Bootstrap
- Beautiful UI with images and videos

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to:
```
http://localhost:5000
```

## Project Structure

```
major-festivals/
├── app.py                 # Main Flask application
├── templates/            # HTML templates
├── static/              # Static files
│   ├── css/            # CSS styles
│   ├── js/             # JavaScript files
│   ├── images/         # Festival images
│   └── videos/         # Festival videos
├── data/               # JSON data files
└── requirements.txt    # Python dependencies
```

## Features in Detail

1. **Start Page**
   - Simple start button to begin the learning journey
   - Timer starts when user enters the home page

2. **Home Page**
   - Festival cards with images and descriptions
   - Navigation to individual festival learning sections
   - Access to the combined quiz

3. **Learning Section**
   - Step-by-step content presentation
   - Progress tracking
   - Interactive elements
   - Media integration (images and videos)

4. **Quiz Section**
   - Multiple choice questions
   - Immediate feedback
   - Score tracking
   - Review of incorrect answers

5. **Timer**
   - 10-minute countdown
   - Visible on all pages
   - Redirects to start page when time expires

## Festival Images

### Diwali
![Diwali Celebration](static/images/Whatsapp-Diwali.jpg)

### Holi
![Holi Festival](static/images/holi1.jpg)
![Holi Celebrations](static/images/holi2.jpg)
![Holi Colors](static/images/holi3.jpg)
![Holi Joy](static/images/holi4.jpg)

### Harvest Festivals
![Harvest Festival](static/images/images1.jpg)
![Festival Celebration](static/images/images11.jpg)

## Technologies Used

- Flask (Python web framework)
- Bootstrap 5 (Frontend framework)
- JavaScript (Timer and interactivity)
- HTML5 & CSS3
- JSON (Data storage)

## Contributing

Feel free to contribute to this project by:
1. Forking the repository
2. Creating a new branch
3. Making your changes
4. Submitting a pull request

## License

This project is licensed under the MIT License.

Copyright (c) 2025 Major Indian Festivals

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Contact

For any questions or suggestions, please open an issue in the repository.

## Acknowledgments

- Thanks to all contributors who help improve this educational platform
- Special thanks to the cultural experts who verified the festival information
- Bootstrap team for their excellent frontend framework
- Flask community for the robust web framework