from Packets.Messages.Client.Login import Login
from Packets.Messages.Client.KeepAlive import KeepAlive
from Packets.Messages.Client.CreateGameroom import CreateGameroom
from Packets.Messages.Client.Exit import Exit
from Packets.Messages.Client.QuitRoom import QuitRoom
from Packets.Messages.Client.AskProfile import AskProfile
from Packets.CommandFactory import Commands

packets = {
    10101: Login,
    10108: KeepAlive,
    14102: Commands,
    14109: Exit,
    14113: AskProfile,
    14350: CreateGameroom,
    14353: QuitRoom
}
