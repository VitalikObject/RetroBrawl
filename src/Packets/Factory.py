from Packets.Messages.Client.ClientHello import ClientHello
from Packets.Messages.Client.Login import Login
from Packets.Messages.Client.KeepAlive import KeepAlive
from Packets.Messages.Client.CreateGameroom import CreateGameroom
from Packets.Messages.Client.Exit import Exit
from Packets.Messages.Client.QuitRoom import QuitRoom
from Packets.Messages.Client.AskProfile import AskProfile
from Packets.Messages.Client.CreateClub import CreateClubMessage
from Packets.Messages.Client.AskJoinableAlliancesMessage import AskJoinableAlliancesMessage
from Packets.Messages.Client.AskClubDataMessage import AskClubData
from Packets.Messages.Client.EditSettingsMessage import EditSettingsMessage
from Packets.Messages.Client.ChangeMap import ChangeMap
from Packets.Messages.Client.AnalyticsEvent import AnalyticsEvent
from Packets.Messages.Client.BattleEnd import BattleEnd
from Packets.Messages.Client.SetName import SetName
from Packets.Messages.Client.ChangeName import ChangeName
from Packets.CommandFactory import EndClientTurn

packets = {
    10100: ClientHello,
    10101: Login,
    10108: KeepAlive,
    10110: AnalyticsEvent,
    10212: SetName,
    14102: EndClientTurn,
    14109: Exit,
    14110: BattleEnd,
    14113: AskProfile,
    # Alliance
    14301: CreateClubMessage,
    14302: AskClubData,
    14303: AskJoinableAlliancesMessage,
    14316: EditSettingsMessage,

    14350: CreateGameroom,
    14353: QuitRoom,
    14363: ChangeMap,
    14600: ChangeName
}
