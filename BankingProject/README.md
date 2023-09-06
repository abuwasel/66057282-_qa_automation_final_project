## Test cases for UI - using (Selenium ,Pytest & Allure reoprts)

```https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login```


1- יש להיכנס למערכת עם אחד מהיוזרים הקיימים לעשות הפקדה של 250 ולראות שהמצב חשבון השתנה בהתאם.

2- כנס למערכת בהרשאות מנהל לחץ על כפתור משתמשים מחק אחד היוזרים לטעמך, כתוב טסט שבודק שהפעולה אכן בוצעה.

3- כנס למערכת בתור מנהל תעשה הוספה ללקוח חדש, תחזור למסך של המנהל ותבדוק שהלקוח שהכנסת אכן נמצא.

4- כנס לבנק בתור משתמש תעשה הפקדה של 1000 שח ומשיכה של 250 תבדוק שמצב החשבון הוא 750.

5- כתוב קוד שנכנס למערכת בתור מנהל ותוסיף חשבון חדש תבדוק שאתה נמצא ב url המתאים.

6- כנס למערכת בתור משתמש תעשה העברה של 1500 יש לוודא שההעברה בוצעה ומופיעה בדו״ח העברות.

7- כנס למערכת עם היוזר של Potter Harry ותוודא שבכל 3 החשבונות שלו יש רק העברה 1

8 כנס למערכת כמנהל ותבדוק שיש לך במערכת בדיוק 5 לקוחות בעזרת הקוד.

9- תעשה בדיקת סאניטי למערכת.

10- בדוק שהמערכת לא נותנת להוסיף לקוח חדש ללא שם פרטי

11- כנס למערכת כיוזר תעשה 3 העברות ותוודא שהסכומים נכונים בדוח ההעברות.

12- כנס למערכת כיוזר בדוק שהשדה של הפקדת כסף אינו מקבל ערכים טקסטואלים רק מספרים.


## To run all the tests and create report directory
```pytest --alluredir=allure_report/ test_selenium.py```

## To run one funtcion test and create report directory
```pytest --alluredir=allure_report/ -k test_login_deposit_250_and_check_balance```

## To run and open allure report
```allure serve "C:\Users\User\PycharmProjects\pythonProject1\pythonProject\qa automation final project\BankingProject\allure_report"```


## How to Install Allure on Windows OS
https://www.youtube.com/watch?v=xdjN-4UxL1c

## Download allure framework
https://github.com/allure-framework/allure2

## Test severity
```
import allure

@allure.epic("Workspaces")
@allure.story("WorkSpaces Creation and Editing Functionality")
@allure.severity(allure.severity_level.NORMAL)
class TestWorkspaces(BaseTest):

      @allure.title("Create new workspace test")
      @allure.description("Create new Workspace")
      def test_severity():
           pass
```
Allure supports next severity levels: ```TRIVIAL```, ```MINOR```, ```NORMAL```, ```CRITICAL``` , ```BLOCKER```. By default, all tests marks with NORMAL severity.

