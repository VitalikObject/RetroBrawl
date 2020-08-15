from Packets.Messages.Client.ClientHello import ClientHello
from Packets.Messages.Client.Login import Login
from Packets.Messages.Client.KeepAlive import KeepAlive
from Packets.Messages.Client.CreateGameroom import CreateGameroom
from Packets.Messages.Client.Exit import Exit
from Packets.Messages.Client.QuitRoom import QuitRoom
from Packets.Messages.Client.AskProfile import AskProfile
from Packets.Messages.Client.OpenClubMessage import OpenClubMessage
from Packets.Messages.Client.ChangeMap import ChangeMap
from Packets.Messages.Client.AnalyticsEvent import AnalyticsEvent
from Packets.CommandFactory import EndClientTurn

packets = {
    10100: ClientHello,
    10101: Login,
    10108: KeepAlive,
    10110: AnalyticsEvent,
    14102: EndClientTurn,
    14109: Exit,
    14113: AskProfile,
    14303: OpenClubMessage,
    14350: CreateGameroom,
    14353: QuitRoom,
    14363: ChangeMap
}
