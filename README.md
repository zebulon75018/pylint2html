# pylint2html
generate html from pylint json file.

pylint.exe -rn --output-format=json pylint2html.py | python pylint2html.py > test.html

* Feature:
  * Group by type
  * Filter by type
  * Filter by content

![ScreenShot](screen.jpg)
