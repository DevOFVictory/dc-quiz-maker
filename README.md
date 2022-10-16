# Discord Quiz Maker
Tools to quickly create PowerPoint Presentation with Quiz-Questions

### Quiz2Json (Scrape Question from the internet)

> Quickly copy quiz questions from the internet and generate python dictionary out of them.

#### How does it work?
1. Install requirements: (`pip3 install <libary>`)
 - pynput
 - pypercli
2. Start application and copy the question first and then the corresponding answer. The app will detect the input automatically when you hit `CTRL+C`
3. When done, hit `ESC` to exit insert mode and export questions to file.


### Json2Powerpoint (Create PowerPoint presentation out of questions)
> Use exported .txt file to create .pptx file with all questions and answers

#### How does it work?
1. Install requirements: (`pip3 install <libary>`)
 - python-pptx
2. Start application to create PowerPoint file named 'Der dümmste fliegt!.pptx'
