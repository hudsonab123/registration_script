# Verify successful lab registration
def isRegistered():
  sourceTMP = s.get('%smodules/group/?course=%s' %(config.URL, config.COURSE))
  soupTMP = bs(sourceTMP.content, 'lxml')
  for group in soupTMP.find_all('td'):
    if (config.DATE['day'] in group.text and config.DATE['time']+'-' in group.text and 'η ομάδα μου' in group.text):
      return True
  return False
