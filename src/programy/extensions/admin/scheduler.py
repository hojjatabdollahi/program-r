from programy.utils.logging.ylogger import YLogger

from programy.extensions.base import Extension


class SchedulerAdminExtension(Extension):

    # execute() is the interface that is called from the <extension> tag in the AIML
    def execute(self, client_context, data):
        YLogger.debug(client_context, "Scheduler Admin - [%s]", data)

        try:
            commands = [x.upper() for x in data.split()]

            if commands[0] == 'COMMANDS':

                return "LIST JOBS, KILL JOB, PAUSE, RESUME"

            elif commands[0] == 'LIST':

                if commands[1] == 'JOBS':
                    jobs = client_context.client.scheduler.list_jobs()
                    if jobs:
                        response = ""
                        for id, job in jobs.items():
                            response += "> Job ID:%s, Next Run: %s, Args: %s\n"%(id, job.next_run_time, str(job.args))
                        return response

                    return "No job information available"

            elif commands[0] == 'KILL':

                if commands[1] == 'JOB':
                    id = commands[2]
                    client_context.client.scheduler.remove_existing_job(id)
                    return "Job removed"

            elif commands[0] == 'PAUSE':
                client_context.client.scheduler.pause()
                return "Scheduler paused"

            elif commands[0] == 'RESUME':
                client_context.client.scheduler.resume()
                return "Scheduler resumed"

        except Exception as e:
            YLogger.exception(client_context, "Failed to execute scheduler extension", e)

        return "Scheduler Admin Error"