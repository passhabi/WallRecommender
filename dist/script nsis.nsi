;NSIS Modern User Interface
;Basic Example Script
;Written by Joost Verburg

;--------------------------------
;Include Modern UI

  !include "MUI2.nsh"

;--------------------------------
;General

  !define VERSION "v1.0.3 beta"

  ;Name and file
  Name "Sama - Wall Recommender - ${VERSION}"
  OutFile "install.exe" 
  Unicode True

  ;icon:
  !define MUI_ICON "install_icon.ico"

  ;Default installation folder
  InstallDir "$PROGRAMFILES32\Sama\Wall Recommender"
  
  ;Get installation folder from registry if available
  InstallDirRegKey HKCU "Software\Sama\Wall Recommender" ""

  ;Request application privileges for Windows Vista
  RequestExecutionLevel admin

;--------------------------------
;Interface Settings

  !define MUI_ABORTWARNING

;--------------------------------
;Pages

  !insertmacro MUI_PAGE_LICENSE "license.txt"
  ; !insertmacro MUI_PAGE_COMPONENTS
  !insertmacro MUI_PAGE_DIRECTORY
  !insertmacro MUI_PAGE_INSTFILES
  
  !insertmacro MUI_UNPAGE_CONFIRM
  !insertmacro MUI_UNPAGE_INSTFILES
  
;--------------------------------
;Languages
 
  !insertmacro MUI_LANGUAGE "English"

;--------------------------------
;Installer Sections

Section "install" SecDummy

  SetOutPath "$INSTDIR"
  
  File /r Program\*

  ;Store installation folder
  WriteRegStr HKCU "Software\Sama\Wall Recommender" "" $INSTDIR
  
  ;Create uninstaller
  WriteUninstaller "$INSTDIR\Uninstall.exe"

  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\WallRecommender" "DisplayName" "Wall Recommender"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\WallRecommender" "UninstallString" '"$INSTDIR\Uninstall.exe"'
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\WallRecommender" "DisplayIcon" '"$INSTDIR\icon.ico"'
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\WallRecommender" "DisplayVersion" '1.0.3 beta'
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\WallRecommender" "Publisher" 'SAMA'
  
  CreateShortcut "$DESKTOP\Sama - Wall Recommender.lnk" "$INSTDIR\samawall.exe"

SectionEnd

;--------------------------------
;Descriptions

  ;Language strings
  LangString DESC_SecDummy ${LANG_ENGLISH} "A test section."

  ;Assign language strings to sections
  !insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
    !insertmacro MUI_DESCRIPTION_TEXT ${SecDummy} $(DESC_SecDummy)
  !insertmacro MUI_FUNCTION_DESCRIPTION_END

;--------------------------------
;Uninstaller Section

Section "Uninstall"

  Delete "$INSTDIR\Uninstall.exe"

  Delete "$DESKTOP\Sama - Wall Recommender.lnk"

  RMDir /r "$INSTDIR"

  DeleteRegKey /ifempty HKCU "Software\Sama - Wall Recommender"

  DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\WallRecommender\"

SectionEnd

!define MUI_STARTMENUPAGE_DEFAULTFOLDER Sama