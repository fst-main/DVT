import logging
from termcolor import colored
from email.mime.multipart import MIMEMultipart
import smtplib





#logger configuration
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="C:\\DevOpsTools_Automation\\Automation%20Platform\\logs\\models.log",
                        level=logging.DEBUG, format=LOG_FORMAT)
logger=logging.getLogger()


class SendMail():

    def __init__(self, message_to_user, message_to_team):
        self.msg = MIMEMultipart()
        self.message_to_user = message_to_user
        self.message_to_team = message_to_team
        self.gbl_address = 'gbl_pwc_it_tool_team@pwc.com'
        self.server = smtplib.SMTP('apprelaycentral.pwcinternal.com:25')


    message_to_user = ""
    message_to_team = ""

    #send mail function
    def send_email_via_smtp(self, message=None , ritm=None, user_address=None ):
        self.msg['From'] = 'automationBOT@pwc.com'
        self.msg['Subject'] = f"RITM : {ritm}"
        self.msg['To'] = f"{self.gbl_address},{user_address}"
        self.msg.attach(message,'plain')
        self.server.sendmail(self.msg['From'], self.msg['To'], self.msg.as_string())
        self.server.quit()
        print (colored("Successfully sent email to:",'green'), self.msg['To'])
        logger.info(f"Successfully sent email to{self.msg['To']}")  


        
