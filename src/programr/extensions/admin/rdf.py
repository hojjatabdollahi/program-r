from programr.utils.logging.ylogger import YLogger

from programr.extensions.base import Extension


class RDFAdminExtension(Extension):

    # execute() is the interface that is called from the <extension> tag in the AIML
    def execute(self, client_context, data):
        YLogger.debug(client_context, "RDF Admin - [%s]", data)

        rdf = ""
        segments = data.split()
        if segments[0] == 'SUBJECTS':
            subjects = client_context.brain.rdf.subjects()
            if segments[1] == 'LIST':
                rdf += "<ul>"
                for subject in subjects:
                    rdf += "<li>%s</li>"%subject
                rdf += "</ul>"
            else:
                return str(len(subjects))

        elif segments[0] == "PREDICATES":
            subject = segments[1]
            predicates = client_context.brain.rdf.predicates(subject)
            rdf += "<ul>"
            for predicate in predicates:
                rdf += "<li>%s</li>" % predicate
            rdf += "</ul>"

        elif segments[0] == "OBJECT":
            subject = segments[1]
            predicate = segments[2]
            objects =  client_context.brain.rdf.objects(subject, predicate)
            rdf += "<ul>"
            for object in objects:
                rdf += "<li>%s</li>" % object
            rdf += "</ul>"

        return rdf