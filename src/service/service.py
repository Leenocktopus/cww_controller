from src.repository.repository import Repository
from src.service import inference_mamdani, model


class Service:
    def __init__(self, repository: Repository):
        self.repository = repository
        inference_mamdani.preprocessing(model.input_lvs, model.output_lv)

    def find_all_names(self):
        return [row[0] for row in self.repository.find_all_names()]

    def save_rating(self, name, results):
        crisp_values = tuple([model.input_lvs[idx]['terms'][i]['centroid'] for idx, i in enumerate(results)])
        rating, decision = inference_mamdani.process(model.input_lvs, model.output_lv, model.rule_base, crisp_values)
        self.repository.save_rating(name, rating, decision)
        return rating, decision

    def find_all_ratings(self):
        return sorted(self.repository.find_all_ratings(), key=lambda x: float(x[1]), reverse=True)
