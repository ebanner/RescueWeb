/**@startuml
hide circles
package personal{
users "1..1"->"0..n" certifications
users "1..1"->"0..1" EMTCert
users "1..1"-->"1..1" operationalStatus
users "1..1"-->"1..1" administrativeStatus
users "0..1"<--"1..1" position
users "1..1"-->"1..1" trainingLevel
users "1..1"-->"1..1" privileges

}
package StandBys{
	standBy "1..1" -> "0..n" standByPersonal
	standByPersonal "0..1" -> "0..1" standByCoverage
}
	users "1..1"-->"0..n" standByPersonal
	users "1..1"-->"0..n" standByCoverage


class users{
	--login--
	<b>userName</b>
	password
	--Name--
	firstName
	middleName
	lastName
	--address--
	street
	city
	state
	zipCode
	--campus Housing--
	residence
	roomNumber
	--ContactInformation--
	phoneNumber
	email
	--SquadInformation--
	<i>privilegeValue</i>
	<i>trainingLevel</i>
	<i>administrativeValue</i>
	<i>operationalValue</i>
	portableNumber
}
class trainingLevel{
	'(none,CPR,EMT-Student,Emt-b,
	' aemt-cc,aemt-p)
	<b><i>trainingValue</b></i>
	trainingLevel
}
class privileges{
	<b><i>privilegeValue</i></b>
	privilege
		'(Admin,Eboard,Member,Guest) 
}
class position{
	'(Eboard Position)
	<b>position</b>
	<i>username</i>
}

class administrativeStatus{
	<b><i>administrativeValue</i></b>
	status
	'(Inactive,Probationary,Observational,Active,EBoard,
	'HonorRoll,Advisor,MedicalDirector)
}

class operationalStatus{
	<b><i>operationalValue</i></b>
	status
	'(Inactive,Probationary,Observational,Active,Active-EMT,
	'ProbationaryCrewChief,CrewChief,MedicalDirector)
}

class certifications{
	<b><i>userName</i></b>
	<b>certification</b>
	expiration
}

class EMTCert{
	<b><i>userName</i></b>
	certNumber
}

class standBy{
	<b>standByID</b>
	event
	location
	notes
	dd
	mm
	yyyy
	time
}

class standByPersonal{
	<b><i>standByID</i></b>
	<b><i>userName</i></b>
	position
	'(ccpic,Active,probationary)
	'Limit by level of training
}

class standByCoverage{
	<b><i>standByID</i></b>
	<b><i>userName</i></b>
	coveredBy
}



@enduml
@enduml
**/
