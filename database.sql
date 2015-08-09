CREATE TABLE skype_contacts (
  handle CHAR(255) PRIMARY KEY     NOT NULL,
  status INTEGER DEFAULT 0

);

CREATE TABLE skype_chats (
  id INTEGER PRIMARY KEY     NOT NULL,
  name TEXT
);


CREATE TABLE skype_messages (
  id INTEGER PRIMARY KEY     NOT NULL,
  body TEXT

);



/*
u.About                               u.IsAuthorized                        u.PhoneHome
u.Aliases                             u.IsBlocked                           u.PhoneMobile
u.Birthday                            u.IsCallForwardActive                 u.PhoneOffice
u.BuddyStatus                         u.IsSkypeOutContact                   u.Province
u.CanLeaveVoicemail                   u.IsVideoCapable                      u.ReceivedAuthRequest
u.City                                u.IsVoicemailCapable                  u.RichMoodText
u.Country                             u.Language                            u.SaveAvatarToFile
u.CountryCode                         u.LanguageCode                        u.SetBuddyStatusPendingAuthorization
u.DisplayName                         u.LastOnline                          u.Sex
u.FullName                            u.LastOnlineDatetime                  u.SpeedDial
u.Handle                              u.MoodText                            u.Timezone
u.HasCallEquipment                    u.NumberOfAuthBuddies
u.Homepage                            u.OnlineStatus
 */