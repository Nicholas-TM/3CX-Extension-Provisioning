import random, string, csv
from datetime import datetime
	
def gen_password():
	pwlist = (
		[
			random.choice(string.digits),
			random.choice(string.ascii_lowercase),
			random.choice(string.ascii_uppercase),
		]  
		+ [
			random.choice(string.ascii_lowercase
			+ string.ascii_uppercase
			+ string.digits) for i in range(7)
		]
	)
	random.shuffle(pwlist)
	return ''.join(pwlist)


def gen_pin():
	return random.randint(1000, 9999)


staff_file_path = input("Staff list file location (*.csv): ")
if not staff_file_path:
	staff_file_path = "staff_list.csv"

school_num = int(input("School Number: "))
start_num = int(input("extension start: "))
if not start_num:
	start_num = 800

staff_extensions = []
with open(staff_file_path) as file:
	#Staff list should have First, Last names, email
	staff_list = csv.DictReader(file, delimiter=',')
	for idx, row in enumerate(staff_list):
		staff_extensions.append(
			[
				str(school_num) + "" + str(start_num+idx), 
				row['First'], 
				row['Last'], 
				row['Email'],
				gen_password(),
				gen_password(),
				str(gen_pin()),
				gen_password(),
				gen_password(),
			]
		)
file.close()
date = datetime.now().strftime("%Y_%m_%d")
output_file = open(staff_file_path[:-3] + "import-" + date +".csv", "w")
output_file.write("Number,FirstName,LastName,EmailAddress,MobileNumber,AuthID,AuthPassword,WebMeetingFriendlyName,WebMeetingPrivateRoom,ClickToCall,WebMeetingAcceptReject,EnableVoicemail,VMNoPin,VMPlayCallerID,PIN,VMPlayMsgDateTime,VMEmailOptions,QueueStatus,OutboundCallerID,SIPID,DeliverAudio,SupportReinvite,SupportReplaces,EnableSRTP,ManagementAccess,ReporterAccess,WallboardAccess,TurnOffMyPhone,HideFWrules,CanSeeRecordings,CanDeleteRecordings,RecordCalls,CallScreening,EmailMissedCalls,Disabled,DisableExternalCalls,AllowLanOnly,BlockRemoteTunnel,PinProtect,MAC_0,InterfaceIP_0,UseTunnel,DND,UseCTI,StartupScreen,HotelModuleAccess,DontShowExtInPHBK,DeskphoneWebPass,SrvcAccessPwd,VoipAdmin,SysAdmin,SecureSIP,PhoneModel14,PhoneTemplate14,CustomTemplate,PhoneSettings,AllowAllRecordings,PushExtension,Integration,AllowOwnRecordings,RecordExternalCallsOnly")
for ext in staff_extensions:
	output_file.write("\n" + ext[0] + "," + ext[1] + "," + ext[2] + "," + ext[3] + ",," + ext[4] + "," + ext[5] + ",,0,0,0,1,1,0," + ext[6] + ",0,2,0,,,0,1,1,0,0,0,,0,0,0,0,0,0,0,0,0,0,0,0,,,1,0,0,0,,0," + ext[7] + "," + ext[8] + ",0,0,0,,,,,0,1,,1,0")
	
output_file.close()
