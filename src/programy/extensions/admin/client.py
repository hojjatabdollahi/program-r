from programy.utils.logging.ylogger import YLogger

from programy.extensions.base import Extension


class ClientAdminExtension(Extension):

    # execute() is the interface that is called from the <extension> tag in the AIML
    def execute(self, client_context, data):
        YLogger.debug(client_context, "Client Admin - [%s]", data)

        try:
            commands = data.split()

            if commands[0] == 'COMMANDS':
                return "LIST BOTS, LIST BRAINS, DUMP BRAIN"

            elif commands[0] == 'LIST':

                if commands[1] == 'BOTS':
                    ids = client_context.client.bot_factory.botids()
                    return ", ".join(ids)

                elif commands[1] == 'BRAINS':
                    botid = commands[2]
                    bot = client_context.client.bot_factory.bot(botid)
                    if bot:
                        ids = bot.brain_factory.brainids()
                        return ", ".join(ids)

                else:
                    return "No client information available"

            elif commands[0] == 'DUMP':

                if commands[1] == 'BRAIN':
                    botid = commands[2]
                    bot = client_context.client.bot_factory.bot(botid)
                    if bot is not None:
                        brainid = commands[3]
                        brain = bot.brain_factory.brain(brainid)
                        if brain is not None:
                            brain.dump_brain_tree()
                            return "Brain dumped, see config for location"

        except Exception as e:
            YLogger.exception(client_context, "Failed to execute client admin extension", e)

        return "Client Admin Error"