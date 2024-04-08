
package com.company.model;

import java.time.LocalDateTime;
import java.util.List;
import org.bonitasoft.engine.bdm.dao.BusinessObjectDAO;

public interface TangDAO
    extends BusinessObjectDAO
{


    public Tang findByPersistenceId(Long persistenceId);

    public List<Tang> findByDatet(LocalDateTime datet, int startIndex, int maxResults);

    public List<Tang> findByStazione(String stazione, int startIndex, int maxResults);

    public List<Tang> findByTraffico(Boolean traffico, int startIndex, int maxResults);

    public List<Tang> findByCausa(String causa, int startIndex, int maxResults);

    public List<Tang> findByOpen_bars(Boolean open_bars, int startIndex, int maxResults);

    public List<Tang> findByAccept(Boolean accept, int startIndex, int maxResults);

    public List<Tang> find(int startIndex, int maxResults);

    public Long countForFindByDatet(LocalDateTime datet);

    public Long countForFindByStazione(String stazione);

    public Long countForFindByTraffico(Boolean traffico);

    public Long countForFindByCausa(String causa);

    public Long countForFindByOpen_bars(Boolean open_bars);

    public Long countForFindByAccept(Boolean accept);

    public Long countForFind();

    public Tang newInstance();

}
