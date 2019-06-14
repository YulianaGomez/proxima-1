"""Engine that performs the model re-training"""

from proxima.data import BaseDataSource
from proxima.inference import BaseInferenceEngine

# TODO (wardlt): Be consistent about what I call the model/surrogate/LFA/learner


class TrainingEngine:
    """Basic model training engine, always retrains the learner"""

    def request_update(self, learner: BaseInferenceEngine, data_source: BaseDataSource) -> bool:
        """Request for the learner to be updated

        Args:
            learner (BaseInferenceEngine): Learned accelerator to be updated
            data_source (BaseDataSource): Link to the data source
        Returns:
            (bool): Whether the model was updated
        """
        X, y = data_source.get_all_data()
        learner.retrain(X, y)
        return True